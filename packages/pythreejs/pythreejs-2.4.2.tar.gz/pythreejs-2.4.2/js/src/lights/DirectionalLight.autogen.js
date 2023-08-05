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

var Object3DModel = require('../core/Object3D.js').Object3DModel;
var LightShadowModel = require('./LightShadow.js').LightShadowModel;

class DirectionalLightModel extends LightModel {

    defaults() {
        return _.extend(LightModel.prototype.defaults.call(this), {

            target: 'uninitialized',
            shadow: 'uninitialized',
            type: "DirectionalLight",

        });
    }

    constructThreeObject() {

        var result = new THREE.DirectionalLight(
            this.convertColorModelToThree(this.get('color'), 'color'),
            this.convertFloatModelToThree(this.get('intensity'), 'intensity')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        LightModel.prototype.createPropertiesArrays.call(this);
        this.three_properties.push('target');
        this.three_properties.push('shadow');

        this.props_created_by_three['type'] = true;
        this.props_created_by_three['matrixWorldNeedsUpdate'] = true;

        this.property_converters['target'] = 'convertThreeType';
        this.property_converters['shadow'] = 'convertThreeType';
        this.property_converters['type'] = null;


    }
}

DirectionalLightModel.model_name = 'DirectionalLightModel';
DirectionalLightModel.serializers = {
    ...LightModel.serializers,
    target: { deserialize: serializers.unpackThreeModel },
    shadow: { deserialize: serializers.unpackThreeModel },
};

module.exports = {
    DirectionalLightModel: DirectionalLightModel,
};
