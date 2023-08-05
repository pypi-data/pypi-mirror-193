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


class AmbientLightModel extends LightModel {

    defaults() {
        return _.extend(LightModel.prototype.defaults.call(this), {

            type: "AmbientLight",

        });
    }

    constructThreeObject() {

        var result = new THREE.AmbientLight(
            this.convertColorModelToThree(this.get('color'), 'color'),
            this.convertFloatModelToThree(this.get('intensity'), 'intensity')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        LightModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['type'] = null;


    }
}

AmbientLightModel.model_name = 'AmbientLightModel';
AmbientLightModel.serializers = {
    ...LightModel.serializers,
};

module.exports = {
    AmbientLightModel: AmbientLightModel,
};
