//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var LightModel = require('./Light.autogen.js').LightModel;


class HemisphereLightModel extends LightModel {

    defaults() {
        return _.extend(LightModel.prototype.defaults.call(this), {

            groundColor: "#000000",
            type: "HemisphereLight",

        });
    }

    constructThreeObject() {

        var result = new THREE.HemisphereLight(
            this.convertColorModelToThree(this.get('color'), 'color'),
            this.convertColorModelToThree(this.get('groundColor'), 'groundColor'),
            this.convertFloatModelToThree(this.get('intensity'), 'intensity')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        LightModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['groundColor'] = 'convertColor';
        this.property_converters['type'] = null;


    }
}

HemisphereLightModel.model_name = 'HemisphereLightModel';
HemisphereLightModel.serializers = {
    ...LightModel.serializers,
};

module.exports = {
    HemisphereLightModel: HemisphereLightModel,
};
