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

var LightShadowModel = require('./LightShadow.js').LightShadowModel;

class PointLightModel extends LightModel {

    defaults() {
        return _.extend(LightModel.prototype.defaults.call(this), {

            power: 12.566370614359172,
            distance: 0,
            decay: 1,
            shadow: 'uninitialized',
            type: "PointLight",

        });
    }

    constructThreeObject() {

        var result = new THREE.PointLight(
            this.convertColorModelToThree(this.get('color'), 'color'),
            this.convertFloatModelToThree(this.get('intensity'), 'intensity'),
            this.convertFloatModelToThree(this.get('distance'), 'distance'),
            this.convertFloatModelToThree(this.get('decay'), 'decay')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        LightModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('shadow');

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['power'] = 'convertFloat';
        this.property_converters['distance'] = 'convertFloat';
        this.property_converters['decay'] = 'convertFloat';
        this.property_converters['shadow'] = 'convertThreeType';
        this.property_converters['type'] = null;


    }
}

PointLightModel.model_name = 'PointLightModel';
PointLightModel.serializers = {
    ...LightModel.serializers,
    shadow: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    PointLightModel: PointLightModel,
};
